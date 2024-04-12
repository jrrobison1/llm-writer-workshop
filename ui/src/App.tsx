import React, { useState } from 'react';
import axios from 'axios';
import './App.css';
import MainEditor from './components/MainEditor';
import WorkshopMember from './components/WorkshopMember';

interface Response {
  role: string;
  review: string;
}

const Header: React.FC = () => {
  return (
    <header className="app-header">
      <h1>LLM Writing Workshop</h1>
      <p>Can you get your creative writing accepted by the publisher? Use your editor, agent, and fellow writer to help you succeed.</p>
    </header>
  );
};

const App: React.FC = () => {
  const [text, setText] = useState('');
  const [models, setModels] = useState<string[]>(['claude-3-haiku-20240307', 'gpt-4', 'claude-3-opus-20240229', 'gpt-3.5-turbo']);
  const [responses, setResponses] = useState<Response[]>(
    [
      { role: 'Editor', review: '' },
      { role: 'Writer', review: '' },
      { role: 'Agent', review: '' },
      { role: 'Publisher', review: '' },
    ]
  );

  const handleSubmit = async () => {
    try {
      const payload = [
        { role: 'Editor', model: models[0] },
        { role: 'Writer', model: models[1] },
        { role: 'Agent', model: models[2] },
        { role: 'Publisher', model: models[3] },
      ];
      const response = await axios.post<Response[]>('http://127.0.0.1:5000/api/v1/generate-reviews', { text, models: payload });
      setResponses(response.data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const handleModelChange = (index: number, model: string) => {
    const updatedModels = [...models];
    updatedModels[index] = model;
    setModels(updatedModels);
  };

  return (
    <>
      <Header />
      <div className="app">
        <div className="sidebar left-sidebar">
          {responses.slice(0, 2).map((response, index) => (
            <WorkshopMember
              key={index}
              role={response.role}
              response={response.review}
              model={models[index]}
              onModelChange={(model) => handleModelChange(index, model)}
            />
          ))}
        </div>
        <MainEditor text={text} setText={setText} onSubmit={handleSubmit} />
        <div className="sidebar right-sidebar">
          {responses.slice(2).map((response, index) => (
            <WorkshopMember
              key={index + 2}
              role={response.role}
              response={response.review}
              model={models[index + 2]}
              onModelChange={(model) => handleModelChange(index + 2, model)}
            />
          ))}
        </div>
      </div>
    </>
  );
};

export default App;
