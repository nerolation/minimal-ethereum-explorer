import React, { useState } from 'react';
import axios from 'axios';
import ReactJson from 'react-json-view';

const App = () => {
    const [blockData, setBlockData] = useState(null);
    const [blockNumber, setBlockNumber] = useState('');

    const fetchData = async () => {
        try {
            const response = await axios.get(`http://localhost:5000/block/${blockNumber}`);
            setBlockData(response.data);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    return (
        <div>
            <h1>Beacon Block Explorer</h1>
            <input
                type="text"
                value={blockNumber}
                onChange={(e) => setBlockNumber(e.target.value)}
                placeholder="Enter Block Number"
            />
            <button onClick={fetchData}>Fetch Block Data</button>

            {blockData && (
                <ReactJson src={blockData} collapsed={true} />
            )}
        </div>
    );
};

export default App;
