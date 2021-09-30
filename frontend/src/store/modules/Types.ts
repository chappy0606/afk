export interface User {
    user: {
        id: number | null
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

export interface Path {
    currentPath: string
}