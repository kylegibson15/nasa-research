export interface Sample {
  bag_number: string;
  generic_description: string;
  generic_id: string;
  has_display: boolean;
  has_thin_section: boolean;
  id: string;
  mission: null;
  mission_id: string;
  original_sample_id: string;
  original_weight: number;
  pristinity: number;
  pristinity_date: Date;
  sample_subtype: string;
  sample_type: string;
}
const SampleCard = ({ sample }: { sample: Sample; }) => {
  return (
    <div style={{ border: '1px solid #ccc', padding: 20, borderRadius: 3, boxShadow: '0 2px 4px rgba(0,0,0,0.1)', margin: 3, maxWidth: 500, minWidth: 300 }}>
      <div style={{ fontWeight: 'bold', marginBottom: 10 }}>
        <p><strong>Sample Type</strong> {sample.sample_type}</p>
        <p><strong>Sample SubType:</strong> {sample.sample_subtype}</p>
      </div>
      <div style={{ marginBottom: 5 }}>
        <p><strong>Original Sample ID:</strong> {sample.original_sample_id}</p>
        <p><strong>Generic ID:</strong> {sample.generic_id}</p>
        <p><strong>Generic Description:</strong> {sample.generic_description}</p>
        <p><strong>Has Display:</strong> {sample.has_display}</p>
        <p><strong>Has Thin Section:</strong> {sample.has_thin_section}</p>
        <p><strong>Original Sample ID:</strong> {sample.original_sample_id}</p>
        <p><strong>Original Weight:</strong> {sample.original_weight}</p>
        <p><strong>Pristinity:</strong> {sample.pristinity}</p>
        <p><strong>Pristinity Date:</strong>{JSON.stringify(sample.pristinity_date)}</p>
      </div>
    </div>
  );
};

export default SampleCard;