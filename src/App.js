import React, { useState, useEffect } from 'react';

function App() {
  const [stores, setStores] = useState([]);

  useEffect(() => {
    // Replace 'YOUR_API_URL' with the actual URL of your Flask API
    fetch('/stores')  // Assuming your API is running on the same domain
      .then(response => response.json())
      .then(data => setStores(data))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  return (
    <div className="store">
      <h1>Store List</h1>
      <ul>
        {stores.map(store => (
          <li key={store._id}>
            <strong>Id:</strong> {store.id}<br />
            <strong>Title:</strong> {store.tilte}
            <strong>Price:</strong>{store.price}
            <strong>Image:</strong>{store.image}

          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
