import React, { useEffect } from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';

import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import NewspaperIcon from '@mui/icons-material/Newspaper';
import Typography from '@mui/material/Typography';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { 
    // Form, 
    // Link, 
    useNavigate } from "react-router-dom";
import { FormControl } from '@mui/material';
// import { AuthContext } from '../context/AuthContext';
import { InputLabel, MenuItem, Select, TextareaAutosize } from '@mui/material';
import { BlogContext } from '../context/BlogContext';

const theme = createTheme();

const NewBlog = () => {
  const navigate = useNavigate()

  const { getCategory, categories, createPost } = React.useContext(BlogContext)

//   const { createUser } = React.useContext(AuthContext)

  const [newBlog, setNewBlog] = React.useState({
    "title": "",
    "category_id": 0,
    "content": "",
    "image": "",
    "status": ""
  });

  useEffect(() => {
    getCategory();
  }, [])

  const handleSubmit = (e) => {
    e.preventDefault();
    createPost(newBlog, navigate);
  }

  return (
    <ThemeProvider theme={theme}>
      <Grid container component="main" sx={{ maxHeight: '91.5vh' }}>
        <CssBaseline />

        <Grid item xs={12} component={Paper} elevation={6} square>

          <Box
            sx={{
              my: 8,
              mx: 4,
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
            }}
          >
            <Avatar sx={{ m: 1, bgcolor: 'darkslategray' }}>
              <NewspaperIcon />
            </Avatar>

            <Typography component="h1" variant="h5" sx={{ color: "tomato" }}>
              New Blog
            </Typography>
            <form onSubmit={handleSubmit}>
              <FormControl>
                <Box sx={{ display: 'flex', flexDirection: 'column', gap: 3.8, width: 350 }}>
                  <TextField
                    label="Title"
                    name="title"
                    id="title"
                    type="text"
                    variant="outlined"
                    required
                    value={newBlog.title}
                    onChange={(e) => setNewBlog({ ...newBlog, "title": e.target.value })}
                  />
                  <FormControl>
                    <InputLabel id="demo-simple-select-helper-label">Categories</InputLabel>
                    <Select
                      labelId="demo-simple-select-helper-label"
                      id="demo-simple-select-helper"
                      name='category'
                      defaultValue=""
                      label="Categories"
                      required
                      value={newBlog.category_id}
                      onChange={(e) => setNewBlog({ ...newBlog, "category_id": e.target.value })}
                    >
                      <MenuItem value="">
                        <em>Categories</em>
                      </MenuItem>
                      {categories?.map((item, index) => (
                        <MenuItem key={index} value={item.id}>{item.name}</MenuItem>
                      ))}
                    </Select>
                  </FormControl>

                  <TextareaAutosize
                    minRows={5}
                    aria-label="Content"
                    placeholder="Content"
                    value={newBlog.content}
                    defaultValue=""
                    required
                    onChange={(e) => setNewBlog({ ...newBlog, "content": e.target.value })}
                  />

                  <TextField
                    label="Image URL"
                    name="image"
                    id="image"
                    type="url"
                    variant="outlined"
                    value={newBlog.image}
                    onChange={(e) => setNewBlog({ ...newBlog, "image": e.target.value })}
                  />
                  <FormControl>
                    <InputLabel id="demo-simple-select-helper-label">Status</InputLabel>
                    <Select
                      labelId="status"
                      id="status"
                      name='status'
                      defaultValue=""
                      label="Status"
                      required
                      value={newBlog.status}
                      onChange={(e) => setNewBlog({ ...newBlog, "status": e.target.value })}
                    >
                      <MenuItem value="">
                        <em>Status</em>
                      </MenuItem>
                      <MenuItem value="d">Draft</MenuItem>
                      <MenuItem value="p">Published</MenuItem>
                    </Select>
                  </FormControl>

                  <Button type="submit" variant="contained" size="large">
                    Send
                  </Button>
                </Box>
              </FormControl>
            </form>
          </Box >

        </Grid >
      </Grid >
    </ThemeProvider >
  )
}

export default NewBlog