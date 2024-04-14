import React from 'react';

interface Props {
  text: string;

  setText: (text: string) => void;
  onSubmit: () => void;
  isLoading: boolean;  // New prop to indicate loading state
}

const MainEditor: React.FC<Props> = ({ text, setText, onSubmit, isLoading }) => {
  return (
    <div className="main-editor">
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Paste your writing here..."
      />
      <div className="submit-area"> {/* Wrapper for button and spinner */}
        <button onClick={onSubmit}>Submit for Review</button>&nbsp;&nbsp;
        {isLoading && <div className="spinner"></div>}
      </div>
    </div>
  );
};

export default MainEditor;