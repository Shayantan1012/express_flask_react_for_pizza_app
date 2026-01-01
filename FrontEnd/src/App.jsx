import Home from './Pages/Home'
import React, { useEffect, useState } from 'react'
import { Route,Routes } from 'react-router-dom'
import Login from './Pages/Auth/Login'
import NotFound from './Pages/pageNotFound'
import Denied from './Pages/Denied'
import AddProduct from './Pages/Admin/AddProduct'
import ProductDetails from './Pages/Products/productDetails'
import CartDetails from './Pages/Cart/cartDeteails'
import Order from './Pages/Order/Order'
import OrderSuccess from './Pages/Order/OrderSuccess'
import RequireAuth from './Components/Auth/RequireAuth'
import { useDispatch, useSelector } from 'react-redux'
import AllProductDetails from './Pages/AllProducts'
import styles from './App.module.scss'
import About from './Pages/About'
import SignUp from './Pages/Auth/SignUP'
import VoiceAssistance from './Pages/VoiceAssistant/VoiceAssi'
import VoiceIcon from './assets/voice.svg'

function App() {

  const dispatch = useDispatch();
  const [popUp,setPopUp]= useState(false);
  const [camInfo,setCamInfo]=useState(false);
  const [welcome, setWelcome] = useState(false);

  function closePopUp() {
        setPopUp(!popUp);
    }



const {cartData}=useSelector((state)=>state.cart);
const { isLoggedIn, role } = useSelector((state) => state.auth);
  let userId=cartData?.user
  useEffect(() => {
    if(isLoggedIn){
    const dfMessenger = document.createElement('df-messenger');
    dfMessenger.setAttribute('intent', 'WELCOME'); // Default intent
    dfMessenger.setAttribute('chat-title', 'WEIGHTER-BOT');
    dfMessenger.setAttribute('agent-id', '55de1bc9-a80e-469a-a7d6-fe2dc2c05b14'); // Your Dialogflow agent ID
    dfMessenger.setAttribute('language-code', 'en');
    dfMessenger.setAttribute('user-id', userId); // Attach dynamic user ID
    document.body.appendChild(dfMessenger); // Append to the DOM
    return () => {
      // Cleanup the component on unmount
      document.body.removeChild(dfMessenger);
    };
  }
}, [isLoggedIn,userId]);

const requireRole=useSelector(state=>state.auth)
  return (
<div className=' bg-gradient-to-r from-white via-gray-100 to-white' >

  { isLoggedIn ?

  <div>
{popUp ? (
  <VoiceAssistance popUp={popUp} closePopUp={closePopUp}  />
) : null}

 {!popUp?
<div className="fixed bottom-6 left-6 z-50">
  <div
    className="montserrat-font1 relative group h-16 w-16"
    onMouseEnter={() => setCamInfo(true)}
    onMouseLeave={() => setCamInfo(false)}
  >
    {/* Tooltip */}
    <div
      className={`
        absolute -top-[88%] left-[18vh] -translate-x-1/2 w-[15rem] px-4 py-2 rounded-lg shadow-lg 
        border border-gray-300 bg-white text-slate-700 transition-all duration-300 ease-in-out 
        z-10 ${camInfo ? 'opacity-100 scale-100' : 'opacity-0 scale-95 pointer-events-none'}
      `}
    >
    <div className=" absolute -bottom-1 left-[5vh] -translate-x-1/2 w-4 h-4 bg-white  border-gray-10 rotate-45"></div>
      Hi , I am a voice assistance !!
    </div>

    {/* Voice Button */}
    <div
      className="h-16 w-16 rounded-full bg-blue-300 shadow-lg hover:bg-blue-400 transition duration-300 flex items-center justify-center cursor-pointer"
      onClick={closePopUp}
    >
      <img src={VoiceIcon} alt="Voice" className="w-3/5 h-3/5 object-contain" />
    </div>
  </div>
</div>:null}

  
</div> :null    
  }


 
<Routes class={styles.appContainer}>
<Route path='/auth/denied' element={<Denied/>}/>
<Route path='/' element={<Home/>}/>
<Route path='/auth/signup' element={<SignUp/>}/>
<Route path='/auth/login' element={<Login/>}/> 
<Route path='/about' element={<About/>}/>
<Route element={<RequireAuth />}>
          <Route path='/order' element={<Order />} />
          <Route path='/order/success' element={<OrderSuccess />} />
          <Route path='/product/:productId' element={<ProductDetails />} />
          <Route path='/cart' element={<CartDetails />} />

          {(requireRole.role === 'ADMIN' )? 
            <Route path='/admin/addproduct' element={<AddProduct />} /> :null
}
        </Route>
        <Route path='/product/allProduct' element={<AllProductDetails/>}/>
        <Route path='*' element={<NotFound/>}/>

</Routes>
    </div>
  )
}
export default App
