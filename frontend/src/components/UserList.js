import React, { useState, useEffect, useCallback } from 'react';
import { List } from 'react-virtualized';
import axios from 'axios';
import './UserList.css';

const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');

const UserList = () => {
    const [users, setUsers] = useState([]);
    const [page, setPage] = useState(1);
    const [selectedLetter, setSelectedLetter] = useState('A');
    const [loading, setLoading] = useState(false);

    const fetchUsers = useCallback(async (letter = selectedLetter, newPage = page) => {
        if (loading) return; // Prevent multiple concurrent loads
        setLoading(true);

        try {
            const response = await axios.get(`http://localhost:5001/users?letter=${letter}&page=${newPage}`);
            if (newPage === 1) {
                setUsers(response.data);
            } else {
                setUsers(prev => [...prev, ...response.data]);
            }
        } catch (error) {
            console.error("Failed to fetch users:", error);
        } finally {
            setLoading(false);
        }
    }, [selectedLetter, page, loading]);

    useEffect(() => {
        fetchUsers(selectedLetter, page);
    }, [fetchUsers, selectedLetter, page]);

    const handleScroll = ({ clientHeight, scrollHeight, scrollTop }) => {
        // Check if we've scrolled to the bottom.
        const isBottom = scrollTop + clientHeight >= scrollHeight - 10;
        if (isBottom && !loading) {
            setPage(prevPage => prevPage + 1);
        }
    };

    const handleLetterClick = (letter) => {
        setSelectedLetter(letter);
        setPage(1); // Reset page to 1 for new letter selection
        setUsers([]); // Clear users for the new letter
    };

    const rowRenderer = ({ key, index, style }) => {
        return (
            <div key={key} style={style} className="user-row">
                {users[index].firstname} {users[index].lastname}
            </div>
        );
    };

    return (
        <div className="user-list-container">
            <div className="alphabet-menu">
                {alphabet.map((letter) => (
                    <button key={letter} onClick={() => handleLetterClick(letter)} className={selectedLetter === letter ? 'selected' : ''}>
                        {letter}
                    </button>
                ))}
            </div>
            <List
                width={500}
                height={600}
                rowCount={users.length}
                rowHeight={20}
                rowRenderer={rowRenderer}
                onScroll={handleScroll}
                overscanRowCount={10}
                style={{outline: 'none'}}
            />
        </div>
    );
};

export default UserList;
