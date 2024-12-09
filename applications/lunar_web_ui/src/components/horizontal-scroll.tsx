const HorizontalScroll = ({ children }: { children: React.ReactNode; }) => {
    return (
        <div style={{ overflowX: 'auto' }}>
            <div style={{ display: 'flex' }}>
                {children}
            </div>
        </div>
    );
};

export default HorizontalScroll;