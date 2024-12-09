import React from 'react';
import './App.css';
import SearchForm, { MissionOptionType } from './components/form';
import MissionCard from './components/mission-card';

function App() {
  const [options, setOptions] = React.useState<MissionOptionType[]>([]);
  const [value, setValue] = React.useState<MissionOptionType | null>(options[0]);
  const [mission, setMission] = React.useState<any>(null);

  React.useEffect(() => {
    fetch('http://localhost:8000/mission-names')
      .then((res) => {
        return res.json();
      })
      .then((missionNames: MissionOptionType[]) => {
        missionNames.sort((a, b) => (a.label > b.label) ? 1 : ((b.label > a.label) ? -1 : 0));
        setOptions(missionNames);
        console.log({ missionNames });
      });
  }, []);

  React.useEffect(() => {
    if (value === null || value === undefined) return;
    console.log({ value });
    fetch(`http://localhost:8000/mission/${value.id}`)
      .then((res) => {
        return res.json();
      })
      .then((mission) => {
        console.log({ mission });
        setMission(mission);
      });
  }, [value]);

  return (
    <div style={{ padding: 5, margin: 5 }}>
      <SearchForm options={options} value={value} setValue={setValue} />
      {mission ? <MissionCard mission={mission} /> : null}
    </div>
  );
}

export default App;
