import * as React from 'react';
import { Card, CardContent, Button, CardActions, Typography, Grid2 as Grid } from '@mui/material';
import HorizontalScroll from './horizontal-scroll';
import SampleCard, { Sample } from './sample-card';
import StationCard, { Station } from './station-card';
import DocumentCard, { ArxivDocument } from './document-card';

export interface Mission {
    id: string;
    name: string;
    samples: Sample[];
    stations: Station[];
    // landmarks: Landmark[];
    documents: ArxivDocument[];
}
export interface MissionCardProps {
    mission: Mission;
}
function MissionCard({ mission: { id, name, samples, stations, documents, ...rest } }: MissionCardProps) {
    console.log({ id, name, samples, stations, rest });
    return (
        <Card>
            <CardContent>
                <Typography gutterBottom variant="h5" component="div">
                    {name}
                </Typography>
            </CardContent>
            <CardActions>
                <Grid>
                    <Grid>
                        <Typography gutterBottom variant="h6" component="div">
                            Samples ({samples.length})
                        </Typography>
                        <HorizontalScroll>
                            {samples.map(sample => <SampleCard sample={sample} />)}
                        </HorizontalScroll>
                    </Grid>

                    <Grid>
                        <Typography gutterBottom variant="h6" component="div">
                            Stations ({stations.length})
                        </Typography>
                        <HorizontalScroll>
                            {stations.map(station => <StationCard station={station} />)}
                        </HorizontalScroll>
                    </Grid>

                    <Grid>
                        <Typography gutterBottom variant="h6" component="div">
                            Related Documents ({documents.length})
                        </Typography>
                        <HorizontalScroll>
                            {documents.map(document => <DocumentCard document={document} />)}
                        </HorizontalScroll>
                    </Grid>
                </Grid>


            </CardActions>
        </Card>
    );
}

export default MissionCard;