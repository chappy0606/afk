export interface User {
    user: {
        id: number | null
        userName: string
    }
    accessToken: string
    refreshToken: string
}

export interface Auth {
    isAuth: boolean | null
}

export interface Path {
    currentPath: string
}