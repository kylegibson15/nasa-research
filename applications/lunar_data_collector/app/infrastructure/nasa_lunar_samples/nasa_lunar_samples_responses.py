from typing import TypedDict

class MissionApiResponse(TypedDict):
    MISSION: str

class StationApiResponse(TypedDict):
    STATION: str

class LandmarkApiResponse(TypedDict):
    LANDMARK: str

class SampleClassificationApiResponse(TypedDict):
    SAMPLETYPE: str
    SAMPLESUBTYPE: str

class SampleApiResponse(TypedDict):
    GENERIC: str
    SAMPLEID: str | None
    MISSION: str
    STATION: str | None
    LANDMARK: str | None
    BAGNUMBER: str
    ORIGINALWEIGHT: float
    SAMPLETYPE: str
    SAMPLESUBTYPE: str | None
    PRISTINITY: float
    PRISTINITYDATE: str
    HASTHINSECTION: bool
    HASDISPLAYSAMPLE: bool | None
    DISPLAYSAMPLENUMBER: None
    GENERICDESCRIPTION: str | None

class SampleThinSectionApiResponse(TypedDict):
    GENERIC: str
    SPECIFIC: str
    WEIGHT: float
    DESCRIPTION: str
    AVAILABILITY: int | float

class SampleDisplayApiResponse(TypedDict):
    REGION: str
    ID: int
    DISPLAYURL: str
    DISPLAYLOCATION: str
    ADD_LINE1: str
    ADD_LINE2: str | None
    ADD_LINE3: str | None
    PHONE: str
    LATITUDE: str
    LONGITUDE: str
    CITY: str
    STATE: str
    COUNTRY: str
    COUNTRYID: str
    ZOOMLEVEL: int
    DISPLAYDESCRIPTION: str
    GENERIC: float 
    SPECIFIC: float