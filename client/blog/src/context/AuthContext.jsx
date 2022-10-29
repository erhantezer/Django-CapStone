import axios from "axios"
import { createContext, useState } from "react"
import React from 'react'
import { toastSuccessNotify } from "../helper/ToastNotify"


//! Defining
export const AuthContext = createContext()



//! Provider

const AuthContextProvider = (props) => {

    const url = "http://127.0.0.1:8000/"

    const [currentUser, setCurrentUser] = useState(sessionStorage.getItem("username") || false)

    const [key, setKey] = useState(sessionStorage.getItem("token") || "")

// ************************** REGISTER *********************

const createUser = async(email, password, firstName, lastName, userName, navigate) => {
    const response = await axios.post(`${url}users/register/`, {

        "username":userName,
        "first_name":firstName,
        "last_name":lastName,
        "email":email,
        "password":password,
        "password1":password,
    })
    console.log(response)
    if(response.data.token){
        setCurrentUser(response.data.username)
        sessionStorage.setItem("username", response.data.username)
        // setKey(response.data.token)
        sessionStorage.setItem("token", response.data.token)
        toastSuccessNotify("User registered success")
        navigate("/")
    }
}

// ************************** LOGIN *********************

const signIn = async(email,password, userName,navigate) => {

    try {
        const res = await axios.post(`${url}users/auth/login/`,{
            "username":userName,
            "email":email,
            "password":password,
        })
        console.log(res)
        
        if(res.data.key){
            setCurrentUser(res.data.user.username)
            sessionStorage.setItem("username", res.data.user.username)
            setKey(res.data.key)
            const myKey = window.btoa(res.data.key)
            sessionStorage.setItem("token", myKey)
            toastSuccessNotify("Login success")
            navigate("/")
        }

    } catch (error) {
        console.log(error)
    }
}

const logout =async(navigate) =>{
    try{
     
     const res = await axios.post(`${url}users/auth/logout/`)
     console.log(res)
     if(res.status===200){
      setCurrentUser(false)
      setKey(false)
      sessionStorage.clear()
      toastSuccessNotify("User logout succesfully")
      navigate("/login")
     }
    }
    catch(err){
      console.log(err)
    }
  }
let values = {
    createUser,
    currentUser,
    key,
    signIn,
    logout,
}

  return (
    <AuthContext.Provider value = {values}>
        {props.children}
    </AuthContext.Provider>
  )
}

export default AuthContextProvider