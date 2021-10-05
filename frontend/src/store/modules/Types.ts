export interface User {
    user: {
        id: number | null
        user_name: string
        created_at: string
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