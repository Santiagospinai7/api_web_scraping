File structure:

.
├── scraper_api  
│   ├── __init__.py   
│   ├── main.py       # Initializes the FastAPI application.
│   ├── dependencies.py  # Defines dependencies (e.g., database session)
│   ├── routers
│   │   ├── __init__.py
│   │   ├── ecommerce.py  # Endpoints for eCommerce-related data
│   │   └── category.py   # Endpoints for category-related data
│   │   └── location.py   # Endpoints for location-related data
│   ├── crud
│   │   ├── __init__.py
│   │   ├── ecommerce.py  # CRUD operations for eCommerce
│   │   └── category.py   # CRUD operations for categories
│   │   └── location.py   # CRUD operations for locations
│   ├── schemas
│   │   ├── __init__.py
│   │   ├── ecommerce.py  # Pydantic models for eCommerce
│   │   └── category.py   # Pydantic models for categories
│   │   └── location.py   # Pydantic models for locations
│   ├── models
│   │   ├── __init__.py
│   │   ├── ecommerce.py  # Database models for eCommerce
│   │   └── category.py   # Database models for categories
│   │   └── location.py   # Database models for locations
│   └── utils
│       ├── __init__.py
│       └── validation.py   # Functions for validation.
├── tests
│   ├── __init__.py
│   ├── test_ecommerce.py
│   ├── test_category.py
│   └── test_location.py
├── requirements.txt
├── .gitignore
└── README.md
