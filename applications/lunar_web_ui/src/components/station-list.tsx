import * as React from 'react';
import { Card, CardContent, Typography } from '@mui/material';
import { Station } from './mission-card';

function StationCard({ station }: { station: Station}) {
  return (
    <Card sx={{ minWidth: 275 }}>
      <CardContent>
        <Typography variant='h5' sx={{ mb: 1.5 }} color="text.secondary">
          station name 
        </Typography>
        <Typography sx={{ mb: 1.5 }} color="text.secondary">
        {station.name}
        </Typography>
        
      </CardContent>
    </Card>
  );
}

function StationList({ stations }: { stations: Station[]}) {
  return (
    <div style={{maxHeight: 400, overflow: 'scroll'}}>
      {stations.map((station) => (
        <StationCard key={station.id} station={station} />
      ))}
    </div>
  );
}

export default StationList;