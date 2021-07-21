export interface User {
    user: {
        id: number | null
        is_active: boolean | null
        is_staff: boolean | null
        password: string
        username: string
        date_joined: string
        email: string
    }
    access_token: string
    refresh_token: string
}

export interface Auth {
    isAuth: boolean | null
}