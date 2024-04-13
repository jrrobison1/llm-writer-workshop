import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import axios from 'axios';
import App from './App';

jest.mock('axios');

describe('App', () => {
  test('renders main editor and workshop members', () => {
    render(<App />);
    expect(screen.getByPlaceholderText('Paste your writing here...')).toBeInTheDocument();
    expect(screen.getByText('Submit for Review')).toBeInTheDocument();
    expect(screen.getAllByRole('combobox')).toHaveLength(4);
    expect(screen.getAllByRole('textbox')).toHaveLength(5);
  });

  test('updates text in main editor', () => {
    render(<App />);
    const textArea = screen.getByPlaceholderText('Paste your writing here...');
    fireEvent.change(textArea, { target: { value: 'Sample text' } });
    expect(textArea).toHaveValue('Sample text');
  });

  test('submits the form and updates responses', async () => {
    const mockResponse = [
      { role: 'Editor', review: 'Editor review' },
      { role: 'Agent', review: 'Agent review' },
      { role: 'Writer', review: 'Writer review' },
      { role: 'Publisher', review: 'Publisher review' },
    ];
    (axios.post as jest.Mock).mockResolvedValueOnce({ data: mockResponse });

    render(<App />);
    const submitButton = screen.getByText('Submit for Review');
    fireEvent.click(submitButton);

    await waitFor(() => {
      expect(screen.getByText('Editor review')).toBeInTheDocument();
      expect(screen.getByText('Agent review')).toBeInTheDocument();
      expect(screen.getByText('Writer review')).toBeInTheDocument();
      expect(screen.getByText('Publisher review')).toBeInTheDocument();
    });
  });

  test('expands workshop member on click', () => {
    render(<App />);
    const workshopMember = screen.getAllByRole('textbox')[1];
    fireEvent.click(workshopMember);
    expect(workshopMember.parentElement).toHaveClass('expanded');
  });

  test('changes model for workshop member', () => {
    render(<App />);
    const modelSelect = screen.getAllByRole('combobox')[0];
    fireEvent.change(modelSelect, { target: { value: 'gpt-4-turbo' } });
    expect(modelSelect).toHaveValue('gpt-4-turbo');
  });
});