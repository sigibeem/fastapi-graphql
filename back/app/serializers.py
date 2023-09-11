from typing import List, Optional

from graphene_pydantic import PydanticInputObjectType, PydanticObjectType
from pydantic import BaseModel


class CommentsModel(BaseModel):
    id: int
    user_id: int
    post_id: int
    body: str


class PostModel(BaseModel):
    id: int
    user_id: int
    todo: str
    description: str
    comments: Optional[List[CommentsModel]]


class UserModel(BaseModel):
    id: int
    name: str
    password: str
    phone_number: str
    email: str
    is_active: bool
    posts: Optional[List[PostModel]]
    comments: Optional[List[CommentsModel]]


class CommentGrapheneModel(PydanticObjectType):
    class Meta:
        model = CommentsModel


class PostGrapheneModel(PydanticObjectType):
    class Meta:
        model = PostModel


class UserGrapheneModel(PydanticObjectType):
    class Meta:
        model = UserModel


class CommentGrapheneInputModel(PydanticInputObjectType):
    class Meta:
        model = CommentsModel
        exclude_fields = ("id",)


class PostGrapheneInputModel(PydanticInputObjectType):
    class Meta:
        model = PostModel
        exclude_fields = ("id", "comments")


class UserGrapheneInputModel(PydanticInputObjectType):
    class Meta:
        model = UserModel
        exclude_fields = ("id", "posts", "comments", "is_active")
