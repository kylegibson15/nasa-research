export interface ArxivDocument {
    arxiv_id: string;
    author: string;
    id: string;
    link: string;
    mission_id: string;
    summary: string;
    title: string;
}
const DocumentCard = ({ document }: { document: ArxivDocument; }) => {
    return (
        <div style={{ border: '1px solid #ccc', padding: 20, borderRadius: 3, boxShadow: '0 2px 4px rgba(0,0,0,0.1)', margin: 3 }}>
            <div style={{ fontWeight: 'bold', marginBottom: 10 }}>
                <p><strong>Title</strong> {document.title}</p>
            </div>
            <div style={{ marginBottom: 5 }}>
                <p style={{ maxWidth: '500px', wordWrap: 'break-word' }}><strong>Summary:</strong> {document.summary}</p>
                <p><strong>Arxiv ID:</strong> {document.arxiv_id}</p>
                <p><strong>Author:</strong> {document.author}</p>
                <p><strong>ID:</strong> {document.id}</p>
                <p><strong>Link:</strong> <a href={document.link} target="_blank">{document.link}</a></p>
            </div>
        </div >
    );
};

export default DocumentCard;