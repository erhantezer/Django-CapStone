import React, { useContext, useEffect } from 'react'
import { AuthContext } from '../context/AuthContext';
import { BlogContext } from '../context/BlogContext';
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardMedia from '@mui/material/CardMedia';
import CardContent from '@mui/material/CardContent';
import CardActions from '@mui/material/CardActions';
import Avatar from '@mui/material/Avatar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import { red } from '@mui/material/colors';
import FavoriteIcon from '@mui/icons-material/Favorite';
import { Badge, Box, Button, Grid } from '@mui/material';
import ChatOutlinedIcon from '@mui/icons-material/ChatOutlined';
import RemoveRedEyeOutlinedIcon from '@mui/icons-material/RemoveRedEyeOutlined';
import { useNavigate } from "react-router-dom";
import { toastErrorNotify } from '../helper/ToastNotify';

const MyPosts = () => {

    const { currentUser } = useContext(AuthContext)

    const { 
        // blogs, 
        getCategory, 
        // categories, 
        page, 
        setPage, 
        usersAllPosts, 
        userPosts } = useContext(BlogContext)

    useEffect(() => {
        getCategory();
        usersAllPosts();
      }, [page])

      const navigate = useNavigate()
      const openDetails = (slug) => {
        if (!currentUser) {
          toastErrorNotify("Login for details of blog!");
        } else {
          navigate(`/details/${slug}`, { state: { slug } })
        }
      }
  return (
    <Box>
      <Box style={{ margin: "2px auto" }}>
        <Box spacing={2}>
          <Box xs={12} md={6} lg={4} xl={3} sx={{ my:3, display:"flex", justifyContent:"center", gap:3, flexWrap:"wrap", mx: "auto" }}>
            {userPosts.map((blog) => (
              <Card sx={{ width: 345, height: 457, position: "relative" }}>
                <CardHeader
                  avatar={
                    <Avatar alt="Emre Sharp" aria-label="blog" sx={{ bgcolor: red[500] }} />
                  }
                  title={blog.author}
                  subheader={blog.last_updated_date.slice(0, 10)}
                />
                <div style={{ cursor: "pointer" }} onClick={() => openDetails(blog.slug)}>

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
                <CardActions disableSpacing sx={{ width: "90%", display: "flex", justifyContent: "space-between", position: "absolute", bottom: "5px", left: "5px" }}>
                  <div>
                    <IconButton aria-label="add to favorites">
                      <FavoriteIcon sx={{ color: (blog.like_post?.filter((like) => like.user_id === currentUser.id)[0]?.user_id) && "red" }} />
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
                  </div>
                  <div>
                    <Badge badgeContent={blog.category} color="primary" sx={{ mx: 2 }} />
                  </div>
                </CardActions>
              </Card>
            ))}
          </Box>
        </Box>
        <Box sx={{ display: "flex", justifyContent: "center", my: 3 }}>
          <Button variant="contained" size="large" onClick={() => setPage(page + 6)} >
            View More...
          </Button>
        </Box>
      </Box>
    </Box>
  )
}

export default MyPosts