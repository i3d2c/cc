# cc
cc is for Constructive Concept, a tool to list components on a 2D plan.

@startuml
[CC (django)] as cc
database Postgres as pg
[OAuth] as auth
[Fabricashape] as fabric
[CC_Graphql] as graphql

cc --> auth : authenticate on
graphql -> auth : authenticate on

cc -up-> fabric : use
cc -> pg : store data in
cc -> graphql : gets data from
@enduml


# Functional specifications

## Components in the screen

1. The 2D zone, where you can import his map and draw your components.
2. The connexion bar, where you see:
    * The connexion button if you're not logged.
    * The account button if you're logged.
3. The main menu
