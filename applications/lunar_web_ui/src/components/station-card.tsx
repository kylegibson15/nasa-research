import * as React from 'react';
import { Card, CardContent, Typography } from '@mui/material';

export interface Station {
  id: string;
  mission_id: string;
  name: string;
}

function StationCard({ station }: { station: Station; }) {
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

export default StationCard;