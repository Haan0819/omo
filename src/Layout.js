import Header from "./Header";
import { Link, Outlet} from 'react-router-dom';
import Footer from './Footer';
import signin_img from './static/images/login.png';
import './App.css';

const Layout = () => {
    return (
        <div>
            <div>
                <header className="navbar">
                    <div className="nav_title"><Link to={'/'} className="nav_title2 linkstyle">Nav</Link></div>
                    <div className="nav_link">
                    <Header />
                    <Link to='/signin' className="signin_link"><img src={signin_img} alt='signinimg'/></Link>
                    </div>
                </header>
                <main className="main_cont">
                    <Outlet />
                </main>    
                <Footer />
            </div>
        </div>
    )
}

export default Layout;