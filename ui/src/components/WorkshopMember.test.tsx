import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import WorkshopMember from './WorkshopMember';

describe('WorkshopMember', () => {
  test('renders role, select, and textarea', () => {
    const props = {
      role: 'Editor',
      response: 'Sample response',
      model: 'gpt-3.5-turbo',
      onModelChange: jest.fn(),
    };
    render(<WorkshopMember {...props} />);
    expect(screen.getByText('Editor')).toBeInTheDocument();
    expect(screen.getByRole('combobox')).toHaveValue('gpt-3.5-turbo');
    expect(screen.getByRole('textbox')).toHaveValue('Sample response');
  });

  test('expands on textarea click', () => {
    const props = {
      role: 'Editor',
      response: 'Sample response',
      model: 'gpt-3.5-turbo',
      onModelChange: jest.fn(),
    };
    render(<WorkshopMember {...props} />);
    const textArea = screen.getByRole('textbox');
    fireEvent.click(textArea);
    expect(textArea.parentElement).toHaveClass('expanded');
  });

  test('calls onModelChange when model is changed', () => {
    const props = {
      role: 'Editor',
      response: 'Sample response',
      model: 'gpt-3.5-turbo',
      onModelChange: jest.fn(),
    };
    render(<WorkshopMember {...props} />);
    const selectElement = screen.getByRole('combobox');
    fireEvent.change(selectElement, { target: { value: 'gpt-4' } });
    expect(props.onModelChange).toHaveBeenCalledWith('gpt-4');
  });
});