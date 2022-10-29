import AppRouter from './router/AppRouter';
import './App.css';
import AuthContextProvider from './context/AuthContext';
import { ToastContainer } from 'react-toastify';
import BlogContextProvider from './context/BlogContext';

function App() {
  return (
    <AuthContextProvider>
      <BlogContextProvider>
      <AppRouter/>
      <ToastContainer />
      </BlogContextProvider>
    </AuthContextProvider>
  );
}

export default App;
