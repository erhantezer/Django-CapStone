import AppRouter from './router/AppRouter';
import './App.css';
import AuthContextProvider from './contexts/AuthContext';
import { ToastContainer } from 'react-toastify';

function App() {
  return (
    <AuthContextProvider>
      <AppRouter/>
      <ToastContainer />
    </AuthContextProvider>
  );
}

export default App;
