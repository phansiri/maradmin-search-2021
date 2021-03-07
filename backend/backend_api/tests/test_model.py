# import json

# from graphene_django.utils.testing import GraphQLTestCase
# from backend_project import schema
# # from backend_api.models import Maradmin

# class MaradminTestCase(GraphQLTestCase):
#     GRAPHQL_SCHEMA = schema.Query

#     def test_all_maradmin_query(self):
#         response = self.query(
#             '''
#             query {
#                 allMaradmins {
#                     edges {
#                         node {
#                             id
#                             number
#                             title
#                             }
#                         }
#                     }
#                 }
#             ''',
#             op_name = 'maradmin'
#         )
#         content = json.loads(response.content)
#         self.assertResponseNoErrors(response)
        

