Movie Review API

A RESTful API built with Django and Django REST Framework to manage movie reviews. Users can create, read, update, and delete (CRUD) reviews, filter reviews by movie title or rating, and sort or paginate results. The API includes user authentication with JWT and permission checks to ensure users can only modify their own reviews.

Features





Review Management: Create, read, update, and delete movie reviews with attributes like Movie Title, Review Content, Rating (1-5), User ID, and Created Date.



User Management: CRUD operations for users with unique Username, Email, and Password.



Authentication: JWT-based authentication to secure endpoints.



Permissions: Only authenticated users can create/update/delete their own reviews; read access is open to all.



Filtering & Sorting: Filter reviews by Movie Title or Rating, and sort by Rating or Date Created.



Pagination: Paginated responses for large datasets (default: 10 reviews per page).
