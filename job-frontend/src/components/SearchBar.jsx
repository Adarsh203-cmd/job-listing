import React from 'react';
import '../styles/SearchBar.css';

const SearchBar = ({ search, handleSearch }) => {
  return (
    <div className="search-bar max-w-md mx-auto mb-6">
      <input
        type="text"
        placeholder="Search jobs by title, company, or location..."
        className="search-input w-full px-4 py-2 border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-300"
        value={search}
        onChange={handleSearch}
      />
    </div>
  );
};

export default SearchBar;
