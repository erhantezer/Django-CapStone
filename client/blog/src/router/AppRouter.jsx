import { useContext } from 'react'
import { 
  BrowserRouter as Router,
  Route,
  Routes,
  Navigate,
  Outlet,
} from 'react-router-dom'
import NavBar from '../components/NavBar'
import { AuthContext } from '../context/AuthContext'
import About from '../pages/About'
import Home from '../pages/Home'
import Login from '../pages/Login'
import MyPosts from '../pages/MyPosts'
import NewBlog from '../pages/NewBlog'
import PostDetails from '../pages/PostDetails'
import Profile from '../pages/Profile'
import Register from '../pages/Register'
import UpdateBlog from '../pages/UpdateBlog'

const AppRouter = () => {
 const {currentUser} = useContext(AuthContext)

  function PrivateRouter() {
    return currentUser ? <Outlet /> : <Navigate to="/login" replace />;
  }

  return (
    <Router>
      <NavBar />
      <Routes>
        <Route path="/" element={<Home />}></Route>
        <Route path="/login" element={<Login />}></Route>

        <Route path="/newblog" element={<PrivateRouter />}>
          <Route path="" element={<NewBlog />} />
        </Route> 

        <Route path="/profile" element={<PrivateRouter />}>
          <Route path="" element={<Profile />} />
        </Route>

        <Route path="/register" element={<Register />}></Route>

        <Route path="/about" element={<About />}/>

        <Route path="/update/:str" element={<PrivateRouter />}>
          <Route path="" element={<UpdateBlog />} />
        </Route>

        <Route path="/details/:str" element={<PrivateRouter />}>
          <Route path="" element={<PostDetails />} />
        </Route>

        <Route path="/myposts" element={<PrivateRouter />}>
          <Route path="" element={<MyPosts />} />
        </Route>
      </Routes>
    </Router>
  )
}

export default AppRouter