import React from "react";
import { Link } from "react-router-dom";
import signin_img from './static/images/login.png'

const SignIn = () => {
    return (
        <div className="container">
            <div className="signin_con">
                <div className="signin_con2">
                    <img src={signin_img} alt='signinimg' />
                    <form className="signin_form">
                        <div className="signin_div"><input type={"text"} placeholder="UserName" className="signin_input" /></div>
                        <div className="signin_div"><input type={"password"} placeholder="PassWord" className="signin_input" /></div>
                        <div className="signin_div"><input type={"submit"} className="signin_btn" value={"로그인"} /></div>
                    </form>
                    <div className="option">
                        <Link className="linkstyle" to='/signup'>회원가입</Link>
                        &nbsp;&nbsp;|&nbsp;&nbsp;
                        <Link className="linkstyle" to='/search'>회원정보 찾기</Link>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default SignIn;