
const initialState = {
    isAuthenticated: false, 
    // Other relevant state properties
  };
  
  const authReducer = (state = initialState, action) => {
    // Handle authentication-related actions here
    switch (action.type) {
      case 'LOGIN':
        return { ...state, isAuthenticated: true };
      case 'LOGOUT':
        return { ...state, isAuthenticated: false };
      default:
        return state;
    }
  };
  
  export default authReducer;
  