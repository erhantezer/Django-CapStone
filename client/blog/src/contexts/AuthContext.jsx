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
        setKey(response.data.token)
        sessionStorage.setItem("token", response.data.token)
        toastSuccessNotify("User registered success")
        navigate("/")
    }
}
let values = {
    createUser,
    currentUser,
    key,
}

  return (
    <AuthContext.Provider value = {values}>
        {props.children}
    </AuthContext.Provider>
  )
}

export default AuthContextProvider