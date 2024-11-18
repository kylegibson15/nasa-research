import * as React from 'react';
import { Card, CardContent, Button, CardActions, Typography } from '@mui/material';
import StationList from './station-list';

export interface Sample {
    bag_number: string
    generic_description: string
    generic_id: string
    has_display: boolean
    has_thin_section: boolean
    id: string
    mission: null
    mission_id: string
    original_sample_id: string
    original_weight: number
    pristinity: number
    pristinity_date: Date
    sample_subtype: string
    sample_type: string
}
export interface Station {
    id: string;
    mission_id: string;
    name: string;
}
export interface Mission {
    id: string;
    name: string;
    samples: Sample[];
    stations: Station[];
}
export interface MissionCardProps {
    mission: Mission;
}
function MissionCard({ mission: { id, name, samples, stations } }: MissionCardProps) {
    return (
        <Card>
            <CardContent>
                <Typography gutterBottom variant="h5" component="div">
                    {name}
                </Typography>
                <Typography variant="body2" sx={{ color: 'text.secondary' }}>
                    Lizards are a widespread group of squamate reptiles, with over 6,000
                    species, ranging across all continents except Antarctica
                </Typography>
            </CardContent>
            <CardActions>
                <Button size="small">Samples</Button>
                <StationList stations={stations} />
            </CardActions>
        </Card>
    );
}

export default MissionCard;