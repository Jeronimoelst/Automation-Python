from Calls_reqres import FirstCallreqresclass

# reqres = FirstCallreqresclass("https://reqres.in/api/unknown/23") 404 NotFound
reqres = FirstCallreqresclass("https://reqres.in/api/users?page=2")
# reqres = FirstCallreqresclass("https://reqres.in/api/users") 201 Created
reqres.GetRequestsVerifyStatusCode()
reqres.GetRequestsVerifyUsers()
reqres.GetRequestsVerifyPage()
reqres.GetRequestsVerifyEmail()
