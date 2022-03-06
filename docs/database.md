# Database

TRV uses Heroku Postgres

## Schema

```mermaid
erDiagram
    events ||--|{ participants: contains
    volunteers ||--|| participants: are

    events {
        int event_id PK
        string title
        string description
        timestamp start
        timestamp end
        string land_manager "JCOS, CT, Lakewood, etc"
        string park
        array trails
        bool public
        string type "Light Maintenance, Project, Cleanup, etc"
        array groups "TRV by default"
    }
    participants {
        int event_id FK
        int volunteer_id FK
        bool attended
    }
    volunteers {
        int volunteer_id PK
        string first_name
        string last_name
        string email
        bool leader
    }
    pictures {
        int event_id
        int picture_id
        string description
        string location
    }
```

## Migrations

TBD