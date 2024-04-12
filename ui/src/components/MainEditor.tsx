import React from 'react';

interface Props {
  text: string;
  setText: (text: string) => void;
  onSubmit: () => void;
}

const MainEditor: React.FC<Props> = ({ text, setText, onSubmit }) => {
  return (
    <div className="main-editor">
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Paste your writing here..."
      />
      <button onClick={onSubmit}>Submit for Review</button>
    </div>
  );
};

export default MainEditor;