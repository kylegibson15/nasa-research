import * as React from 'react';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';

export interface MissionOptionType {
    label: string;
    id: string;
}

export interface SearchFormProps {
    options: MissionOptionType[];
    value: MissionOptionType | null;
    setValue: React.Dispatch<React.SetStateAction<MissionOptionType | null>>;
}

export default function SearchForm({ options, value, setValue }: SearchFormProps) {
    return (
        <Autocomplete
            options={options}
            id="auto-highlight"
            autoHighlight
            value={value}
            onChange={(_: any, newValue: MissionOptionType | null) => {
                setValue(newValue);
            }}
            renderInput={(params) => (
                <TextField {...params} label="select lunar mission" variant="standard" />
            )}
        />
    );
}


