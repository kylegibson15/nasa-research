A good report should address the following:

- [x] High level description of application developed for project.
- [x] Whiteboard architecture diagram and description of the diagram.
    - [x] You should discuss the processes and services in the diagram.
- [x] Justifications for design decisions.
    - [x] Example: Why NoSQL database chosen over SQL database?

- [ ] system requirements for the project as well as 
    - [ ] how testable those requirements were.

## High Level Application Description

My project, NASA Research, is composed of;
- two python services (data collection and data analysis)
- a react/typescript webapp
- event messaging
- PostgreSQL database
- prometheus monitoring
- grafana analytics dashboard

![Diagram](./nasa-research-project.png)

The application collects data from the NASA Lunar Samples API and links all the objects (Missions, Landmarks, Stations, Samples, Sample Display's) to the mission that they are associated with. The data is stored in a PostgreSQL database. 

There is also a separate service that runs in parallel that performs analysis on the Lunar Samples data and also queries the Arxiv API for documentst that are related to the Mission. This service also performs more analysis on the data collected from the Lunar Samples API by gathering metrics on the data in the database (ex. count number of each of the objects).

To trigger analyzing and adding Arxiv documents, these two services communicate via SQS event messaging and utilizing the same PostgreSQL database. 

The data collector service first queries the Lunar Sample API and with each mission, the mission name is sent via a message and the data analysis service picks up the message off of the queue. Once the data analysis service has received the message it will do a lookup of the mission via its name from the database. The data analysis service, then queries the Arxiv API and updates the PostgreSQL database with a relationship between a Arxiv document and the mission.

The Web UI servers to give a user friendly interface in querying and interacting with the data.

There is also a Prometheus server and Grafana Web Dashboard running that monitors the health of the overall system.

There were a few architectural decisions that were made throughout the development of the application. First of which was to use PostgreSQL as the database technology. The data that I am working with has a very clear structure and clear relationships between objects. This allows for defining a clear database schema. I chose PostgreSQL over other SQL technologies because I am most familiar with its apis and configuration. 

Another decision was to break the data analysis service out of the data collection service. I made this decision to have a clear separation of concern between performing analysis and collecting data. Though the data analysis service does collect data from the Arxiv API it is to support and provide more information on the mission that has been already collected. I also wanted to reduce the load of work that the data collection service would be performing considering it also hosts the APIs that allow the Web UI to query for the Missions data. 

