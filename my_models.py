from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator

class User(Model):
    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=50)
    last_name = fields.CharField(max_length=50)
    joindate = fields.DateField(auto_now_add=True)
    password_hash = fields.CharField(max_length=128 , null=False)

User_Pydantic = pydantic_model_creator(User,name='User')
UserIn_Pydantic = pydantic_model_creator(User,name="UserIn", exclude_readonly=True)

