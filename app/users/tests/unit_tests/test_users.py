# import pytest
# from sqlalchemy.exc import IntegrityError

# from app.tests import TestClass, TestingSessionLocal
# from app.users.exceptions.exceptions import UserNotFoundException
# from app.users.repository import UserRepository


# class TestUserRepo(TestClass):
#     def create_users_for_methods(self):
#         with TestingSessionLocal() as db:
#             user_repository = UserRepository(db)
#             user = user_repository.create_user(
#                 "John", "Smith", "jsmith1@gmail.com", "password1234"
#             )
#             user = user_repository.create_user(
#                 "John", "Smith", "jsmith2@gmail.com", "password1234"
#             )
#             user = user_repository.create_user(
#                 "John", "Smith", "jsmith3@gmail.com", "password1234"
#             )
#             user = user_repository.create_user(
#                 "John", "Smith", "jsmith4@gmail.com", "password1234"
#             )

#     def test_create_user(self):
#         with TestingSessionLocal() as db:
#             user_repository = UserRepository(db)
#             user = user_repository.create_user(
#                 "John", "Smith", "jsmith@gmail.com", "password1234"
#             )
#             assert user.email == "jsmith@gmail.com"
#             assert user.is_superuser is False
#             assert user.is_active is True

#     def test_create_user_duplicate_error(self):
#         with TestingSessionLocal() as db:
#             user_repository = UserRepository(db)
#             user = user_repository.create_user(
#                 "John", "Smith", "jsmith@gmail.com", "password1234"
#             )
#             assert user.is_active is not False
#             with pytest.raises(IntegrityError) as e:
#                 user1 = user_repository.create_user(
#                     "John", "Smith", "jsmith@gmail.com", "password1234"
#                 )

#     def test_create_super_user(self):
#         with TestingSessionLocal() as db:
#             user_repository = UserRepository(db)
#             super_user = user_repository.create_super_user(
#                 "James", "Marshall", "jmarshall@gmail.com", "password1234"
#             )
#             assert super_user.email == "jmarshall@gmail.com"
#             assert super_user.is_superuser is True
#             assert super_user.is_active is True

#     def test_create_super_user_duplicate_error(self):
#         with TestingSessionLocal() as db:
#             user_repository = UserRepository(db)
#             super_user = user_repository.create_super_user(
#                 "James", "Marshall", "jmarshall@gmail.com", "password1234"
#             )
#             assert super_user.is_superuser is not False
#             with pytest.raises(IntegrityError) as e:
#                 user1 = user_repository.create_super_user(
#                     "James", "Marshall", "jmarshall@gmail.com", "password1234"
#                 )

#     def test_get_user_by_id(self):
#         with TestingSessionLocal() as db:
#             user_repository = UserRepository(db)
#             user = user_repository.create_user(
#                 "James", "Marshall", "jmarshall@gmail.com", "password1234"
#             )
#             user1 = user_repository.get_user_by_id(user.id)
#             assert user.id == user1.id
#             assert user.name == user1.name
#             assert user.surname == user1.surname
#             assert user.email == user1.email

#     def test_get_user_by_id_error_not_found(self):
#         with TestingSessionLocal() as db:
#             user_repository = UserRepository(db)
#             user = user_repository.create_user(
#                 "James", "Marshall", "jmarshall@gmail.com", "password1234"
#             )
#             with pytest.raises(UserNotFoundException) as e:
#                 user1 = user_repository.get_user_by_id("false_user_id")

#     def test_get_all_users(self):
#         self.create_users_for_methods()
#         with TestingSessionLocal() as db:
#             user_repository = UserRepository(db)
#             all_users = user_repository.get_all_users()
#             assert len(all_users) == 4

#     def test_delete_user_by_id(self):
#         with TestingSessionLocal() as db:
#             user_repository = UserRepository(db)
#             user = user_repository.create_user(
#                 "John", "Smith", "jsmith2@gmail.com", "password1234"
#             )
#             assert user_repository.delete_user_by_id(user.id) is True

#     def test_delete_user_by_id_error_not_found(self):
#         with TestingSessionLocal() as db:
#             user_repository = UserRepository(db)
#             user = user_repository.create_user(
#                 "John", "Smith", "jsmith2@gmail.com", "password1234"
#             )
#             with pytest.raises(UserNotFoundException) as e:
#                 user1 = user_repository.delete_user_by_id("false_user_id")

#     def test_update_user_is_active(self):
#         with TestingSessionLocal() as db:
#             user_repository = UserRepository(db)
#             user = user_repository.create_user(
#                 "John", "Smith", "jsmith2@gmail.com", "password1234"
#             )
#             user = user_repository.update_user_is_active(user.id, False)
#             assert user.is_active is False

#     def test_update_user_is_active_error_not_found(self):
#         with TestingSessionLocal() as db:
#             user_repository = UserRepository(db)
#             user = user_repository.create_user(
#                 "John", "Smith", "jsmith2@gmail.com", "password1234"
#             )
#             with pytest.raises(UserNotFoundException) as e:
#                 user = user_repository.update_user_is_active("false_user_id", False)

#     def get_user_by_email(self):
#         with TestingSessionLocal() as db:
#             user_repository = UserRepository(db)
#             user = user_repository.create_user(
#                 "John", "Smith", "jsmith2@gmail.com", "password1234"
#             )
#             assert user.email == "jsmith2@gmail.com"

#     def test_get_user_by_email_error_not_found(self):
#         with TestingSessionLocal() as db:
#             user_repository = UserRepository(db)
#             user = user_repository.create_user(
#                 "John", "Smith", "jsmith2@gmail.com", "password1234"
#             )
#             with pytest.raises(UserNotFoundException) as e:
#                 user = user_repository.get_user_by_email("false_email")

#     def test_create_user_email_integrity_error(self):
#         with TestingSessionLocal() as db:
#             user_repository = UserRepository(db)
#             with pytest.raises(IntegrityError) as e:
#                 user = user_repository.create_user(
#                     "John", "Smith", None, "password1234"
#                 )

#     def test_create_user_name_integrity_error(self):
#         with TestingSessionLocal() as db:
#             user_repository = UserRepository(db)
#             with pytest.raises(IntegrityError) as e:
#                 user = user_repository.create_user(
#                     None, "Smith", "jsmith2@gmail.com", "password1234"
#                 )

#     def test_create_user_surname_integrity_error(self):
#         with TestingSessionLocal() as db:
#             user_repository = UserRepository(db)
#             with pytest.raises(IntegrityError) as e:
#                 user = user_repository.create_user(
#                     "John", None, "jsmith2@gmail.com", "password1234"
#                 )

#     def test_create_user_password_integrity_error(self):
#         with TestingSessionLocal() as db:
#             user_repository = UserRepository(db)
#             with pytest.raises(IntegrityError) as e:
#                 user = user_repository.create_user(
#                     "John", "Smith", "jsmith2@gmail.com", None
#                 )
