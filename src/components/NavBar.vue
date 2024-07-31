<!-- src/components/NavBar.vue -->
<template>
  <header class="header">
    <nav class="nav container">
      <div class="nav__data">
        <router-link to="/" class="nav__logo"><i class="ri-planet-line"></i> TNCO</router-link>
              
            <div class="nav__toggle" id="nav-toggle">
              <i class="ri-menu-line nav__burger"></i>
              <i class="ri-close-line nav__close"></i>
            </div>
      </div>
      <div class="nav__menu" id="nav-menu" >
          <ul class="nav__list">
            <li><router-link to="/search-ip" class="nav__link">Search IP</router-link></li>
            <li class="dropdown__item" >
              <div class="nav__link">
                Reconcile <i class="ri-arrow-down-s-line dropdown__arrow"></i>
              </div>
            
              <ul class="dropdown__menu" >
                <li><router-link  :to="{ name: 'page_reconcile', params: { id: 'daily_report' }}" class="dropdown__link"><i class="ri-time-line"></i> Daily Report</router-link></li>

                <!-- <li><router-link to="/reconcile/daily_report" class="dropdown__link"><i class="ri-time-line"></i> Daily Report</router-link></li> -->
                

                <!--=============== DROPDOWN SUBMENU ===============-->
                <li class="dropdown__subitem">
                    <div class="dropdown__link">
                      <i class="ri-base-station-line"></i> BGP <i class="ri-add-line dropdown__add"></i>
                    </div>

                    <ul class="dropdown__submenu">
                        <li><router-link :to="{ name: 'page_reconcile', params: { id: 'iBGP' }}" class="dropdown__sublink"><i class="ri-route-line"></i> iBGP</router-link></li>
                        <li><router-link :to="{ name: 'page_reconcile', params: { id: 'eBGP' }}" class="dropdown__sublink"><i class="ri-route-fill"></i> eBGP</router-link></li>
                    </ul>
                </li>
                <li><router-link :to="{ name: 'page_reconcile', params: { id: 'status_L2' }}" class="dropdown__link"><i class="ri-signal-tower-line"></i> Status L2</router-link></li>
                
                <li><router-link :to="{ name: 'page_reconcile', params: { id: 'vrrp' }}" class="dropdown__link"><i class="ri-pie-chart-line"></i> VRRP</router-link></li>

                <li class="dropdown__subitem">
                  <div class="dropdown__link">
                    <i class="ri-send-backward"></i> ACL <i class="ri-add-line dropdown__add"></i>
                  </div>
                  <ul class="dropdown__submenu">
                        <li><router-link :to="{ name: 'page_reconcile', params: { id: 'acl' }}" class="dropdown__sublink"><i class="ri-focus-line"></i> Compare ACL</router-link></li>
                        <li><router-link :to="{ name: 'page_reconcile', params: { id: 'acl_bgp' }}" class="dropdown__sublink"><i class="ri-focus-3-line"></i> Compare ACL BGP</router-link></li>
                  </ul>
                </li>
                <li class="dropdown__subitem">
                  <div class="dropdown__link">
                    <i class="ri-bar-chart-line"></i> Service <i class="ri-add-line dropdown__add"></i>
                  </div>
                  <ul class="dropdown__submenu">
                    <li><router-link :to="{ name: 'page_reconcile', params: { id: 'services_L2' }}" class="dropdown__sublink"><i class="ri-stack-line"></i> Service L2</router-link></li>
                    <li><router-link :to="{ name: 'page_reconcile', params: { id: 'services_L3' }}" class="dropdown__sublink"><i class="ri-stack-fill"></i> Service L3</router-link></li>
                  </ul>
                </li>

                <li><router-link :to="{ name: 'page_reconcile', params: { id: 'network-queue' }}" class="dropdown__link"><i class="ri-bubble-chart-line"></i> Network Queue</router-link></li>
                <li><router-link :to="{ name: 'page_reconcile', params: { id: 'infra' }}" class="dropdown__link"><i class="ri-settings-line"></i> Infra</router-link></li>
              </ul>
            </li>
            <li><router-link to="/something" class="nav__link">something</router-link></li>
            <hr class="sep">
            <li class="nav__user"><i class="ri-account-circle-line"></i> Username</li>
            <li class="nav__logout"><router-link to="/something" class="btn-logout"><i class="ri-logout-box-line"></i>Logout</router-link></li>
            </ul>
        </div>
        <!-- <div class="nav__menu">
          <i class="ri-account-circle-line"></i> Username
          <li class="nav__link"><router-link to="/Firstpage"><i class="ri-logout-box-line"></i>Logout</router-link></li>    
      </div> -->

    </nav>
  </header>
    
  </template>
  
<script>
  document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.getElementById('nav-toggle'),
          nav = document.getElementById('nav-menu')
 
    toggle.addEventListener('click', () =>{
        // Add show-menu class to nav menu
        nav.classList.toggle('show-menu')
 
        // Add show-icon to show and hide the menu icon
        toggle.classList.toggle('show-icon')
    })
  });
export default {
  name: 'NavBar',
};
</script>
  
<style scoped>

/*=============== HEADER ===============*/
.header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background-color: var(--white-color-light);
    box-shadow: 0 2px 16px hsla(220, 32%, 8%, .3);
    z-index: var(--z-fixed);
}

.nav__logout{
  height: 100%;
}

.btn-logout{
  cursor: pointer;
  border: none;
  outline: none;
  border-radius: 24px;
  border-style: none;
  border-color: #ee3434;
  height: 32px !important;
  color: white;
  padding: 1rem 1.5rem !important;
  background-color: inherit;
  font-family: inherit;
  margin: 0;
  font-size: medium; 
  font-weight: bold;
  position: relative;
  text-align: center;
  text-transform: none;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  will-change: transform,opacity;
  z-index: 0;
  border: 2px solid #1e1d1d!important;
}

.btn-logout:hover{
  background-color: #ee3434;
  color: white;
  background-position: 0 100%;
  border: 2px solid #ee3434!important;
}
  
  /*=============== NAV ===============*/
  .nav {
    height: var(--header-height);
  }
  
  .nav__logo, 
  .nav__burger, 
  .nav__close {
    color: var(--black-color);
  }
  
  .nav__data {
    height: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .nav__logo {
    display: inline-flex;
    align-items: center;
    column-gap: .25rem;
    font-weight: var(--font-semi-bold);
    /* Color highlighting when pressed on mobile devices */
    /*-webkit-tap-highlight-color: transparent;*/
  }
  
  .nav__logo i {
    font-weight: initial;
    font-size: 1.25rem;
  }
  
  .nav__toggle {
    position: relative;
    width: 32px;
    height: 32px;
  }
  
  .nav__burger, 
  .nav__close {
    position: absolute;
    width: max-content;
    height: max-content;
    inset: 0;
    margin: auto;
    font-size: 1.25rem;
    cursor: pointer;
    transition: opacity .1s, transform .4s;
  }
  
  .nav__close {
    opacity: 0;
  }

  hr{
    display: none;
  }
  
  /* Navigation for mobile devices */
  @media screen and (max-width: 1118px) {
    .nav__menu {
      position: absolute;
      left: 0;
      top: 2.5rem;
      width: 100%;
      max-height: 100dvh;
      overflow: auto;
      pointer-events: none;
      opacity: 0;
      transition: top .4s, opacity .3s;
      background-color: var(--white-color);
      box-shadow: 2px 6px 16px -4px hsl(0deg 0% 49.61% / 30%);
    }
    .nav__menu::-webkit-scrollbar {
      width: 0;
    }
    .nav__list {
      background-color: var(--black-color);
      padding-top: 1rem;
    }
    .nav__user, .nav__logout{
      justify-content:left;
    }
    .nav__user > i, .nav__logout>a>i {
      display: none;
    }

    .btn-logout{
      border: none !important;
      padding: 0 !important;
      height: min-content !important;
      width: 100%;
    }

    hr.sep {
      display: flex;
      border: 0;
      border-bottom: 2px dashed #ccc;
      background: #999;
  }

    .nav__logout:hover, .btn-logout:hover{
      background-color: #ee3434 !important;
      color: white;
      border-radius: 0;
      width: 100%;
    }

    
  }
  
  .nav__link, .nav__user, .nav__logout, .btn-logout {
    color: var(--black-color);
    background-color: var(--while-color-light);
    font-weight: var(--font-semi-bold);
    padding: 1.25rem 13vw;
    display: flex;
    justify-content:space-between;
    align-items: center;
    transition: background-color .3s;
  }

  .nav__user, .nav__logout{
    justify-content: flex-start;
    background-color: var(--grey) !important;
  }

  li .nav__user > i {
    display: none;
  }
  
  .nav__link:hover {
    background-color: var(--grey-color);
  }

  .nav__logout>a:hover{
    background-color: #ee3434;
  }
  
  /* Show menu */
  .show-menu {
    opacity: 1;
    top: 3.5rem;
    pointer-events: initial;
  }
  
  /* Show icon */
  .show-icon .nav__burger {
    opacity: 0;
    transform: rotate(90deg);
  }
  .show-icon .nav__close {
    opacity: 1;
    transform: rotate(90deg);
  }
  
  /*=============== DROPDOWN ===============*/
  .dropdown__item {
    cursor: pointer;
  }
  
  .dropdown__arrow {
    font-size: 1.25rem;
    font-weight: initial;
    transition: transform .4s;
  }
  
  .dropdown__link, 
  .dropdown__sublink {
    color: var(--black-color);
    background-color: var(--white-color);
    display: flex;
    align-items: center;
    column-gap: .5rem;
    font-weight: var(--font-semi-bold);
    transition: background-color .3s;
  }

  .dropdown__sublink {
    background-color: var(--grey-color-light);
  }
  
  .dropdown__link{
    padding: 1.25rem 13vw 1.25rem 16vw;
  }
  
  .dropdown__sublink {
    padding: 1.25rem 13vw 1.25rem  19vw;
  }
  
  .dropdown__link i, 
  .dropdown__sublink i {
    font-size: 1.25rem;
    font-weight: initial;
  }
  
  .dropdown__link:hover, 
  .dropdown__sublink:hover {
    background-color: var(--grey-color);
  }
  
  .dropdown__menu, 
  .dropdown__submenu {
    max-height: 0;
    overflow: hidden;
    transition: max-height .4s ease-out;
    box-shadow: s 16px 16px hsla(220, 32%, 8%, .3);


  }
  
  /* Show dropdown menu & submenu */
  .dropdown__item:hover .dropdown__menu, 
  .dropdown__subitem:hover > .dropdown__submenu {
    max-height: 1000px;
    transition: max-height .4s ease-in;
  }
  
  /* Rotate dropdown icon */
  .dropdown__item:hover .dropdown__arrow {
    transform: rotate(180deg);
  }
  
  /*=============== DROPDOWN SUBMENU ===============*/
  .dropdown__add {
    margin-left: auto; 
  }
  
  .dropdown__sublink {
    background-color: var(--grey);
  }
  
  /*=============== BREAKPOINTS ===============*/
  /* For small devices */
  @media screen and (max-width: 340px) {
    .container {
      margin-inline: 1rem;
    }
  
    .nav__link, .nav__user, .nav__logout,.btn-logout {
      padding-inline: 1rem;
    }

   
  }
  
  /* For large devices */
  @media screen and (min-width: 1118px) {
    .container {
      margin-inline: auto;
    }
  
    .nav {
      height: calc(var(--header-height) + 1rem);
      display: flex;
      justify-content: space-between;
    }
    .nav__toggle {
      display: none;
    }
    .nav__list {
      height: 100%;
      display: flex;
      column-gap: 3rem;
    }
    .nav__link, .nav__user, .nav__logout, .btn-logout {
      height: 100%;
      padding: 0;
      justify-content: initial;
      column-gap: .25rem;
      background-color: var(--while-color-light) !important;
    }

    .btn-logout:hover {
      border: 1px solid #ee3434;
      background-color: #ee3434 !important;
    }
    .nav__link:hover {
      background-color: transparent;
      opacity: 1;
    }

    
  
    .dropdown__item, 
    .dropdown__subitem {
      position: relative;
    }
  
    .dropdown__menu, 
    .dropdown__submenu {
      max-height: initial;
      overflow: initial;
      position: absolute;
      left: 0;
      top: 6rem;
      width: max-content;
      opacity: 0;
      pointer-events: none;
      transition: opacity .3s, top .3s;
    }
  
    .dropdown__link, 
    .dropdown__sublink {
      padding-inline: 1rem 3.5rem;
      background: var(--grey-color-light);
  }
    
  
    .dropdown__subitem .dropdown__link {
      padding-inline: 1rem;
    }

    .dropdown__add {
      margin-left: auto;
    }

  
    .dropdown__submenu {
      position: absolute;
      left: 100%;
      top: .5rem;
    }
  
    /* Show dropdown menu */
    .dropdown__item:hover .dropdown__menu {
      opacity: 1;
      top: 4.5rem;
      pointer-events: initial;
      transition: top .3s;
    }
  
    /* Show dropdown submenu */
    .dropdown__subitem:hover > .dropdown__submenu {
      opacity: 1;
      top: 0;
      pointer-events: initial;
      transition: top .3s;
    }
  }
  </style>
  