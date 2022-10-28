import React, { useContext, useState } from 'react'
import { useEffect } from 'react'
import { useLocation, useNavigate } from 'react-router-dom'
import { BlogContext } from '../context/BlogContext'
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
import { AuthContext } from '../context/AuthContext';
import { Button, Divider, InputAdornment, List, ListItem, ListItemText, TextField } from '@mui/material';

const PostDetails = () => {

  const [likeColor, setLikeColor] = useState(false);
  const [comment, setComment] = useState();
  const { getOneBlog, blogDetail, detailLoading, setComments, deletePost } = useContext(BlogContext)
  const { currentUser } = useContext(AuthContext)
  const { state } = useLocation()

  const navigate = useNavigate()

  const handleChange = (e) => {
    e.preventDefault();
    const value = e.target.value;
    setComment(value);
  }

  const handleSubmit = (e) => {
    e.preventDefault();
    setComments(state.slug, comment);
    setComment("");
  }

  useEffect(() => {
    getOneBlog(state.slug)
  }, [])

  const base_url = "http://127.0.0.1:8000/"

  const token = window.atob(sessionStorage.getItem('token'));

  const like = async () => {
    var data = {
      "user_id": currentUser.id,
      "post": blogDetail.id
    };
    var config = {
      method: 'post',
      url: `${base_url}api/like/`,
      headers: {
        'Authorization': `Token ${token}`,
      },
      data: data
    }
    try {
      const x = await axios(config)
      getOneBlog(state.slug);
      setLikeColor(!likeColor)
    } catch (error) {
      console.log(error)
    }
  }
  const handleFavorite = () => {
    like()
  }

  return (
    <div>
      {detailLoading ? (
        <Box sx={{ display: 'flex' }}>
          <CircularProgress />
        </Box>
      ) : (
        <Box style={{ display: "flex", alignItem: "center", justifyContent: "center", position: "relative" }}>
          <Box sx={{ maxWidth: { xs: "100%", sm: "80%", md: "70%" }, minWidth:{ xs: "100%", sm: "80%", md: "40%" }, marginX: "auto",}}>

            <CardMedia
              height="500px"
              component="img"
              image={blogDetail.image}
              alt={blogDetail.title}
            />

            <CardHeader
              avatar={
                <Avatar sx={{ bgcolor: red[500] }} alt={blogDetail.author} aria-label="blog">
                </Avatar>
              }
              title={blogDetail.author}
              subheader={blogDetail.last_updated_date.slice(0, 10)}
            />
            <CardContent>
              <Typography variant="body2" color="text.secondary">
                {blogDetail.title}
              </Typography>
              <Typography variant="body2" color="text.secondary">
                {blogDetail.content}
              </Typography>
            </CardContent>
            <CardActions disableSpacing sx={{ bottom: "5px", left: "5px" }}>
              <IconButton aria-label="add to favorites">
                <FavoriteIcon onClick={() => handleFavorite()} sx={{ color: (blogDetail.like_post?.filter((like) => like.user_id === currentUser.id)[0]?.user_id) && "red" }} />
                <Typography sx={{ marginLeft: 1 }}>
                  {blogDetail.like_count}
                </Typography>
              </IconButton>
              <IconButton aria-label="comment">
                <ChatOutlinedIcon />
                <Typography sx={{ marginLeft: 1 }}>
                  {blogDetail.comment_count}
                </Typography>
              </IconButton>
              <IconButton aria-label="view">
                <RemoveRedEyeOutlinedIcon />
                <Typography sx={{ marginLeft: 1 }}>
                  {blogDetail.post_view_count}
                </Typography>
              </IconButton>
            </CardActions>

            {blogDetail.author_id === currentUser.id && <Box sx={{ my: 3, display: "flex", gap: 3 }}>
              <Button variant="contained" size="small" color="success" onClick={()=>navigate(`/update/${state.slug}`, {state: {blogDetail}})}>Update Blog</Button>
              <Button variant="contained" size="small" color="error" onClick={()=> deletePost(navigate, state.slug) }>Delete Blog</Button>
            </Box>}

            <Box>
              <List sx={{ width: '100%', maxWidth: 360, bgcolor: 'background.paper' }}>
                {blogDetail.comment_post.map((comment) => (
                  <>
                    <ListItem alignItems="flex-start">
                      <ListItemText
                        primary={comment.user}
                        secondary={
                          <React.Fragment>
                            <Typography
                              sx={{ display: 'inline', mr: 2 }}
                              component="span"
                              variant="body4"
                              color="text.secondary"
                            >
                              {(new Date(comment.time_stamp).toUTCString()).slice(0, 16)}
                            </Typography>
                            <Typography
                              component="p"
                              variant="body1"
                              color="text.primary">
                              {comment.content}
                            </Typography>
                          </React.Fragment>
                        }
                      />
                    </ListItem>
                    <Divider variant="inset" component="li" />
                  </>
                ))}
              </List>
            </Box>

            <form onSubmit={handleSubmit}>
              <Box sx={{ display: 'flex', flexDirection: 'column', gap: 3.8 }}>
                <TextField
                  label="Comment"
                  name="comment"
                  id="comment"
                  type="text"
                  variant="outlined"
                  multiline
                  rows={6}
                  maxRows={18}
                  placeholder='Add a comment'
                  value={comment}
                  onChange={handleChange}
                  InputProps={{
                    startAdornment: (
                      <InputAdornment position='start' ></InputAdornment>
                    )
                  }}
                />
                <Button type="submit" variant="contained" size="large">
                  Add Comment
                </Button>
              </Box>
            </form>
          </Box>
        </Box>
      )

      }

    </div>
  )
}

export default PostDetails;