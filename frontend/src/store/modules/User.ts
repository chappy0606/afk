export interface User {
    id: number | null
    username: string
    password: string
    email: string
    is_staff: boolean
    is_active: boolean
    date_joined: string
    token: {
        accessToken: string
        refreshToken: string
    }
}