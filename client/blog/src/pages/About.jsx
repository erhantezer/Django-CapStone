import { Box, Typography } from '@mui/material'
import React from 'react'

const About = () => {
  return (
    <Box sx={{ height: "calc(100vh - 70px)", width: "100%", backgroundImage: 'url("https://images.unsplash.com/photo-1625838144804-300f3907c110?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80")' }}>

      <Box sx={{ display: "flex", textAlign:"center", padding:{xs:"1rem", sm: "7% 7% 0 7%" , md: "10% 10% 0 10%", xl:"15% 15% 0 15%"}}}>
        <Typography variant="h5" sx={{ color: "white"}}>
        On this blog page; you can create blogs in the categories of "Home, Holiday, Cars, Sports, Health, People, History, Cities, Technology" and get information from blogs created by other users. Happy blogging...
        </Typography>
      </Box>
    </Box>
  )
}

export default About