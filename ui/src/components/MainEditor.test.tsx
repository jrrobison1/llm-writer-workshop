import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import MainEditor from './MainEditor';

describe('MainEditor', () => {
  test('renders textarea and submit button', () => {
    const props = {
      text: '',
      setText: jest.fn(),
      onSubmit: jest.fn(),
    };
    render(<MainEditor {...props} />);
    expect(screen.getByPlaceholderText('Paste your writing here...')).toBeInTheDocument();
    expect(screen.getByText('Submit for Review')).toBeInTheDocument();
  });

  test('updates text in textarea', () => {
    const props = {
      text: '',
      setText: jest.fn(),
      onSubmit: jest.fn(),
    };
    render(<MainEditor {...props} />);
    const textArea = screen.getByPlaceholderText('Paste your writing here...');
    fireEvent.change(textArea, { target: { value: 'Sample text' } });
    expect(props.setText).toHaveBeenCalledWith('Sample text');
  });

  test('calls onSubmit when submit button is clicked', () => {
    const props = {
      text: '',
      setText: jest.fn(),
      onSubmit: jest.fn(),
    };
    render(<MainEditor {...props} />);
    const submitButton = screen.getByText('Submit for Review');
    fireEvent.click(submitButton);
    expect(props.onSubmit).toHaveBeenCalled();
  });
});