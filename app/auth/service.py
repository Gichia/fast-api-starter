"""
The auth service file to implement auth endpoints functionalities.

Classes:

    None

Functions:

    register_user(db, first_name, email, password):
        register new user details.

Misc variables:

    None
"""
from datetime import datetime, timedelta

from jose import JWTError, jwt
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status

from app import models, config
from app.users import schema, service, repository


settings = config.Settings()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_password_hash(password: str) -> str:
    """
    Return a password hash

    Parameters:
    ----------
        password: str:
            the password to be hashed.

    Returns:
    -------
        hashed_password:
            the hashed password
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Method to verify if passwords match

    Parameters:
    ----------
        plain_password: str:
            the plain text password.
        hashed_password: str
            the hashed password

    Returns:
    -------
        bool: True if the password match False if not
    """
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """
    Method to create JWT access token for logged in user

    Parameters:
    ----------
        data: Dict
            a dictionary with email the email as sub
        expires_delta: timedelta
            the number of minutes the token will be valid for.

    Returns:
    -------
        access_token: The generated access token
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        claims=to_encode,
        key=settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)) -> str:
    """
    Method to get the current logged in user.
    Decodes the token and returns the sub which is the email.

    Parameters:
    ----------
        token: str
            the access token provided

    Returns:
    -------
        email: The email of the logged in user

    Raises
    ------
        HTTPException:
            if the token is invalid or has expired
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token,
                             settings.SECRET_KEY,
                             algorithms=[settings.ALGORITHM]
                             )
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    return email


async def register_user(
        db: Session, user: schema.UserCreate) -> models.User:
    """
    Save a new user details to the database.

    Parameters:
    ----------
        db: (Session):
            the database session to be used.
        user: (schema.UserCreate):
            the default user details.

    Returns:
    -------
        User:
            the newly created user details
    """
    existing_user = await repository.get_by_email(db=db, email=user.email)

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="That email is already in use",
        )

    hashed_password = create_password_hash(password=user.password)
    user.password = hashed_password

    return await service.create_user(db=db, user=user)


async def login(email: str, plain_password: str, db: Session):
    """
    Method to log in a user

    Parameters:
    ----------
        email: str
            the email of user trying to log in
        plain_password: str
            plain password to be checked.

    Returns:
    -------
        access_token: The generated access token

    Raises
    ------
        HTTPException:
            Authorization error if invalid credentials are supplied.
    """
    error = False

    user = await service.get_by_email(db=db, email=email)

    if not user:
        error = True

    if not error and not verify_password(
            plain_password=plain_password, hashed_password=user.password):
        error = True

    if error:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials")

    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

    return {
        "token_type": "bearer",
        "access_token": access_token,
        "expires_in": access_token_expires.total_seconds(),
    }
