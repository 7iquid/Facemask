// import { Popover } from '@headlessui/react'
// import React, { useState } from 'react'
// import './tailwind.css';

// route
// import Login from "../routes/account/login";
// import Menu from "../routes/menu/menu";
import MyTabs from "./dropdownmenu";


export default function NavKo() {

    return (
      <div className='py-1 text-white 
          bg-gradient-to-l from-gray-800 to-black
          flex justify-between relative'>
        <div className=' px-1 text-left'>
          <h1 className='font-mono text-2xl  '> FACTS-TECH</h1> 
          <p className='text-left text-sm'>Mechatronics Enterprises</p> 
        </div>
        <div className='mobile-menu-button  py-1 px-4 focus:outline-none focus:bg-gray-700'>
          <MyTabs />
        </div>
      </div>
    );
}


