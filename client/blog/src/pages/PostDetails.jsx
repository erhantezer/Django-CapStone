import React, { useContext } from 'react'
import { useEffect } from 'react'
import { useLocation, useParams } from 'react-router-dom'
import { BlogContext } from '../contexts/BlogContext'
// import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardMedia from '@mui/material/CardMedia';
import CardContent from '@mui/material/CardContent';
import CardActions from '@mui/material/CardActions';
import Avatar from '@mui/material/Avatar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import { red } from '@mui/material/colors';
import FavoriteIcon from '@mui/icons-material/Favorite';
import ChatOutlinedIcon from '@mui/icons-material/ChatOutlined';
import RemoveRedEyeOutlinedIcon from '@mui/icons-material/RemoveRedEyeOutlined';
import CircularProgress from '@mui/material/CircularProgress';
import Box from '@mui/material/Box';
import axios from 'axios';
import { AuthContext } from '../contexts/AuthContext';
import { useState } from 'react';
import { Card, Grid } from '@mui/material';

const PostDetails = () => {
  const { slug } = useParams();
  const { blogDetail,blogs } = useContext(BlogContext)
  const { currentUser } = useContext(AuthContext)
  const [details, setDetails] = useState([])
  const [loading, setLoading] = useState(false)
  const { state } = useLocation()
  console.log(state)
  console.log(blogDetail)
  console.log(currentUser)

  const base_url = "http://127.0.0.1:8000/"
  async function getOneBlog() {
    const token = window.atob(sessionStorage.getItem('token'));
    setLoading(true)
    try {
      var config = {
        method: 'get',
        url: `${base_url}api/posts/${slug}`,
        headers: {
          'Authorization': `Token ${token}`,
        }
      };
      const result = await axios(config);
      console.log(result)
      setTimeout(()=>{
        setLoading(false)
      },3000)
      
      setDetails(result.data);
      console.log(details)
      
    } catch (error) {
      console.log(error)
    }
  }

  console.log(details)

 useEffect(() => {

getOneBlog()

 }, [])
 
  
  

  const token = window.atob(sessionStorage.getItem('token'));

  const like = async () => {
    var data = {
      "user_id": currentUser.id,
      "post": blogDetail.id
    };
console.log("Like isteği yapıldı.");
    var config = {
      method: 'post',
      url: `${base_url}api/like/`,
      headers: {
        'Authorization': `Token ${token}`,
      }
    }
    const x = await axios(`${base_url}api/like/`, data, config)
    console.log(x)
  }
  const handleFavorite = () => {
    like()
  }
console.log("rendering")
  return (
    <>
      {loading ? (
        <Box sx={{ display: 'flex' }}>
          <CircularProgress />
        </Box>
      ) : (
        
        <div>
      <Grid container spacing={2} justifyContent="center" sx={{ mt: 2 }}>
        {details.map((blog) => (
          <Grid item xs={12} md={6} lg={4} xl={3}>
            <Card sx={{ maxWidth: 345, height: 457, position: "relative" }}>
              <CardHeader
                avatar={
                  <Avatar alt="Emre Sharp" aria-label="blog" sx={{ bgcolor: red[500] }} />

                }
                title={blog.author}
                subheader={blog.last_updated_date.slice(0, 10)}
              />
              <div style={{ cursor: "pointer" }} >

                <CardMedia
                  component="img"
                  height="194"
                  image={blog.image}
                  alt={blog.title}
                />
                <CardContent>
                  <Typography gutterBottom variant="h5" component="div">
                    {blog.title}
                  </Typography>
                  <Typography sx={{
                    overflow: 'hidden',
                    textOverflow: 'ellipsis',
                    display: '-webkit-box',
                    WebkitLineClamp: '3',
                    WebkitBoxOrient: 'vertical',
                  }} variant="body2" color="text.secondary">
                    {blog.content}
                  </Typography>
                </CardContent>
              </div>
              <CardActions disableSpacing sx={{ position: "absolute", bottom: "5px", left: "5px" }}>
                <IconButton aria-label="add to favorites">
                  <FavoriteIcon />
                  <Typography sx={{ marginLeft: 1 }}>
                    {blog.like_count}
                  </Typography>
                </IconButton>
                <IconButton aria-label="comment">
                  <ChatOutlinedIcon />
                  <Typography sx={{ marginLeft: 1 }}>
                    {blog.comment_count}
                  </Typography>
                </IconButton>
                <IconButton aria-label="view">
                  <RemoveRedEyeOutlinedIcon />
                  <Typography sx={{ marginLeft: 1 }}>
                    {blog.post_view_count}
                  </Typography>
                </IconButton>
              </CardActions>
            </Card>

          </Grid>))}
      </Grid>

    </div>
        // <Box style={{ display: "flex", alignItem: "center", justifyContent: "center", position: "relative" }} sx={{ maxWidth: { xs: "100%", sm: "80%", md: "60%" }, marginX: "auto" }}>
        //   { details.map((item)=>(
        //   <Box>
        //     console.log(item);

        //     <CardMedia
        //       component="img"
        //       height="300"
        //       image={item.image}
        //       alt={item.title}
        //     />
        //     <CardHeader
        //       avatar={
        //         <Avatar sx={{ bgcolor: red[500] }} alt={item.author} aria-label="blog">
        //         </Avatar>
        //       }
        //       title={item.author}
        //       subheader={blogDetail.last_updated_date.slice(0, 10)}
        //     />
        //     <CardContent>
        //       <Typography variant="body2" color="text.secondary">
        //         {item.title}
        //       </Typography>
        //       <Typography variant="body2" color="text.secondary">
        //         {item.content}
        //       </Typography>
        //     </CardContent>
        //     <CardActions disableSpacing sx={{ bottom: "5px", left: "5px" }}>
        //       <IconButton aria-label="add to favorites">
        //         <FavoriteIcon onClick={() => handleFavorite()} sx={{ color: "red" }} />
        //         <Typography sx={{ marginLeft: 1 }}>
        //           {item.like_count}
        //         </Typography>
        //       </IconButton>
        //       <IconButton aria-label="comment">
        //         <ChatOutlinedIcon />
        //         <Typography sx={{ marginLeft: 1 }}>
        //           {item.comment_count}
        //         </Typography>
        //       </IconButton>
        //       <IconButton aria-label="view">
        //         <RemoveRedEyeOutlinedIcon />
        //         <Typography sx={{ marginLeft: 1 }}>
        //           {item.post_view_count}
        //         </Typography>
        //       </IconButton>
        //     </CardActions>
        //   </Box>))
        //   }
          
        // </Box>
      )}
    </>
  )
}

export default PostDetails;