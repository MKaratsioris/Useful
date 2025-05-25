"""
OAuth 2.0 Code Grant Flow

       User                       Client                     Authorization Server          Resource Server
1.      |-----Access application--->|                               |                             |
2.      |                           |------------Redirect---------->|                             |
3.      |<---------------------Authenticate-------------------------|                             |
4.      |--------------Authentication credentials------------------>|                             |
5.      |<-----------------Request authorization--------------------|                             |
6.      |-------------------Grant authorization-------------------->|                             |
7.      |                           |<-----Authorization code-------|                             |
8.      |                           |-----Request access token----->|                             |
9.      |                           |<--Access token+Refresh token--|                             |
10.     |                           |--------------Request resource with access token------------>|
11.     |                           |<----------------------Protected resource--------------------|

"""
